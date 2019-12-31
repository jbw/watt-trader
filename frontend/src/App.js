import React, { useState } from 'react';
import useAxios from 'axios-hooks'
import '@fortawesome/fontawesome-free/css/all.css'
import Select from "react-dropdown-select";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Badge from 'react-bootstrap/Badge';
import Spinner from 'react-bootstrap/Spinner';
import { MDBDataTable } from 'mdbreact';
import ReactGA from 'react-ga';



const LoadingSpinner = () => {
  return (
    <div className="d-flex justify-content-center">
      <Spinner variant="primary" animation="border" role="status">
        <span className="sr-only">Loading...</span>
      </Spinner>
    </div>
  )
}

function TraderStockCard(props) {

  const { trs, name } = props.stock;

  return (
    <>
      <Card.Header><i className="far fa-map"></i> {name}</Card.Header>

      <ListGroup >
        {
          trs.map(
            (tr) => {

              return (

                <ListGroup.Item key={tr.code}>
                  <Row>
                    <Col>

                      <Badge variant="primary" style={{ float: 'left' }} >
                        {tr.name}
                      </Badge>
                    </Col>
                    <Col>
                      <Badge variant="secondary" style={{ float: 'right', }}>
                        {tr.code}
                      </Badge>
                    </Col>
                    <Col>
                      <Badge pill variant="warning" style={{ float: 'right' }}>
                        {tr.cost} W
                      </Badge>
                    </Col>
                  </Row>

                </ListGroup.Item>

              )
            }
          )
        }
      </ListGroup>
    </>
  )
}

function App() {

  ReactGA.pageview('watt.jbw.dev', ['watt']);

  const [selectedTR, setSelectedTR] = useState({ id: 0, name: 'Swords Dance' })
  const [selectedTrader, setSelectedTrader] = useState({ id: 0, name: 'Meetup Spot' })

  const [{ data: stock, loading: stock_loading, error: stock_error }] = useAxios(
    `/api/stock/${selectedTrader.id}/${selectedTR.id}`
  )

  const [{ data: traders, loading: traders_loading, error: traders_error }] = useAxios(
    '/api/traders'
  )
  const [{ data: trs, loading: trs_loading, error: trs_error }] = useAxios(
    '/api/trs'
  )


  if (stock_error || traders_error || trs_error) return <p>Error!</p>

  const onTRChange = (values) => setSelectedTR(values[0])

  const onTraderChange = (values) => setSelectedTrader(values[0])

  return (

    <Container>
      <Row>
        <Jumbotron style={{ width: '100%' }}>

          <h1>Watt Trader TR Finder</h1>
          <p>Find all the TRs available from Watt Traders across in-game locations select or search below.</p>
          <ul>
            <li>A Watt Trader's stock will reshuffle every couple of days.</li>
            <li>You must always select the <strong>first</strong> TR in a Watt Traders list for this to work. <a target="_blank" rel="noopener noreferrer" href="https://i.imgur.com/XN8i6Tt.jpg">See example.</a></li>
          </ul>
          <strong>Tip:</strong> use the in game map to find the locations.
        </Jumbotron>
      </Row>
      {trs_loading || traders_loading ? <LoadingSpinner /> :
        <Row className="justify-content-md-center">

          <Card border="light" style={{ minWidth: '20rem', maxWidth: '50rem', margin: '0.5rem' }}>

            <Select style={{ minWidth: '20rem' }}
              placeholder={'Trader location e.g. Meetup Spot'}
              loading={traders_loading}
              options={traders}
              values={[traders[0]]}
              labelField={'name'}
              sortBy={'id'}
              valueField={'id'}
              onChange={(values) => onTraderChange(values)}
            />
          </Card>

          <Card border="light" style={{ minWidth: '20rem', maxWidth: '50rem', margin: '0.5rem' }} >
            <Select style={{ minWidth: '20rem' }}
              placeholder={'First TR code (TR00-TR49)'}
              loading={trs_loading}
              searchable={true}
              options={trs}
              values={[trs[0]]}

              labelField={'name'}
              searchBy={'code'}
              sortBy={'id'}
              valueField={'id'}
              onChange={(values) => onTRChange(values)}
            />
          </Card>

        </Row>
      }

      <Row style={{ justifyContent: 'center', marginTop: '2rem' }}>

        {!stock_loading &&
          <>
            {
              stock['stock'].map(s =>
                <Card key={s.trader_id} bg="light" style={{ minWidth: '25rem', maxWidth: '50rem', margin: '0.5rem' }}>
                  <TraderStockCard stock={s} />
                </Card>
              )
            }
          </>
        }
      </Row>

      {!stock_loading &&
        <Row className="justify-content-md-center">

          <Container style={{ width: '100%' }}>

            <div style={{ marginTop: '2rem', marginBottom: '1.5rem' }}>
              <h3>Not in circulation</h3>
              <p>Below is a table of TRs which are not currently available in game given the current selection of <strong>{selectedTrader.name}</strong> and <strong>{selectedTR.name}</strong>.</p>
            </div>

            <MDBDataTable
              striped
              barReverse

              info={false}
              noBottomColumns
              data={{
                columns: [
                  {
                    label: 'Name',
                    field: 'name',
                    sort: 'asc',
                  },
                  {
                    label: 'Code',
                    field: 'code',
                    sort: 'asc',
                  },
                  {
                    label: 'Cost',
                    field: 'cost',
                    sort: 'asc',

                  }
                ], rows: stock['not_in_circulation']
              }}
            />
          </Container>
        </Row>
      }
    </Container >
  );
}

export default App;
