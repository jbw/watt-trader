import React, { useState } from 'react';
import useAxios from 'axios-hooks'
import '@fortawesome/fontawesome-free/css/all.css'
import Select from "react-dropdown-select";
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Badge from 'react-bootstrap/Badge'
import Spinner from 'react-bootstrap/Spinner'


const LoadingSpinner = () => {
  return (
    <Spinner variant="primary" animation="border" role="status">
      <span className="sr-only">Loading...</span>
    </Spinner>
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

  const [selectedTRId, setSelectedTRId] = useState(0)
  const [selectedTraderId, setSelectedTraderId] = useState(0)

  const [{ data: stock, loading: stock_loading, error: stock_error }, refetch] = useAxios(
    `/api/stock/${selectedTraderId}/${selectedTRId}`
  )

  const [{ data: traders, loading: traders_loading, error: traders_error }] = useAxios(
    '/api/traders'
  )
  const [{ data: trs, loading: trs_loading, error: trs_error }] = useAxios(
    '/api/trs'
  )

  if (stock_error || traders_error || trs_error) return <p>Error!</p>

  const onTRChange = (values) => setSelectedTRId(values[0].id)

  const onTraderChange = (values) => setSelectedTraderId(values[0].id)

  return (

    <Container>
      <Row>
        <Jumbotron style={{ width: '100%' }}>

          <h1>Watt Trader</h1>
          <p>To show all the TRs available from Watt Traders across in game locations select or search below.</p>
          <ul>
            <li>A Watt Trader's stock will reshuffle every couple of days.</li>
            <li>You must always select the <strong>first</strong> TR in a Watt Traders list for this to work. <a target="_blank" rel="noopener noreferrer" href="https://i.imgur.com/XN8i6Tt.jpg">See example</a></li>
          </ul>
          <strong>Tip:</strong> Use the in game map to find the locations.

        </Jumbotron>
      </Row>

      <Row className="justify-content-md-center">

        <Card border="light" style={{ minWidth: '20rem', maxWidth: '50rem', margin: '0.5rem' }}>

          <Select style={{ minWidth: '20rem' }}
            placeholder={'Trader location e.g. Meetup Spot'}
            loading={traders_loading}
            options={traders}
            labelField={'name'}
            sortBy={'id'}
            valueField={'id'}
            onChange={(values) => onTraderChange(values)}
          />
        </Card>
        <Card border="light" style={{ minWidth: '20rem', maxWidth: '50rem', margin: '0.5rem' }} >
          <Select style={{ minWidth: '20rem' }}
            placeholder={'TR code e.g. TR99'}
            loading={trs_loading}
            searchable={true}
            options={trs}
            labelField={'name'}
            searchBy={'code'}
            sortBy={'id'}
            valueField={'id'}
            onChange={(values) => onTRChange(values)}
          />
        </Card>
        <Card border="light" style={{ margin: '0.5rem' }}>
          <Button variant="dark" onClick={refetch}>Find</Button>
        </Card>
      </Row>
      <Row style={{ justifyContent: 'center', marginTop: '2rem' }}>

        {stock_loading ? <LoadingSpinner /> :
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
    </Container >
  );
}

export default App;
