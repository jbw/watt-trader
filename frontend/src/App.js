import React, { useState } from 'react';
import useAxios from 'axios-hooks'
import Select from "react-dropdown-select";
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import Jumbotron from 'react-bootstrap/Jumbotron';

import Badge from 'react-bootstrap/Badge'

function TraderStockCard(props) {

  const { trs, name } = props.stock;


  return (
    <>
      <Card.Header>{name}</Card.Header>

      <ListGroup >
        {
          trs.map(
            (tr) => {

              return (

                <ListGroup.Item >
                  <Row>
                    <Col>

                      <Badge pill variant="dark" style={{ float: 'left' }} >
                        {tr.name}
                      </Badge>
                    </Col>
                    <Col>
                      <Badge pill variant="info" style={{ float: 'right', }}>
                        {tr.code}
                      </Badge>
                    </Col>
                    <Col>
                      <Badge pill variant="dark" style={{ float: 'right' }}>
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
          <p>To show all the TRs available from Watt Traders across in game locations for the current schedule select or search below.</p>
          <p>You must always select the <strong>first</strong> TR in a Watt Traders list for this to work.</p>
        </Jumbotron>
      </Row>

      <Row className="justify-content-md-center">
        <Col xs sm={4}>
          <Select
            placeholder={'Trader location e.g. Meetup Spot'}

            loading={traders_loading}
            options={traders}
            labelField={'name'}
            sortBy={'id'}
            valueField={'id'}
            onChange={(values) => onTraderChange(values)}
          />
        </Col>
        <Col xs sm={4}>
          <Select
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
        </Col>
        <div>
          <Button onClick={refetch}>Find</Button>

        </div>



      </Row>
      <Row style={{ justifyContent: 'center', marginTop: '2rem' }}>

        {stock_loading ? <p>Loading..</p> :
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
