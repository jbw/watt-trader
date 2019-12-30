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
import '@fortawesome/fontawesome-free/css/all.css';

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

      <Jumbotron>
        <h1>Watt Trader</h1>
        <p>Select the first TR from a Watt Trader then press 'find' all the TRs available for the current schedule.</p>
      </Jumbotron>

      <Row className="justify-content-md-center">
        <Col sm>
          <Select
            placeholder={'Search by TR code e.g. TR99'}
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
        <Col sm>
          <Select
            loading={traders_loading}
            options={traders}
            labelField={'name'}
            sortBy={'id'}
            valueField={'id'}
            onChange={(values) => onTraderChange(values)}
          />
        </Col>
        <Col sm>
          <Button onClick={refetch}>Find</Button>
        </Col>
      </Row>

      <Row style={{ marginTop: '2rem' }}>

        {stock_loading ? <p>Loading..</p> :
          <>
            {
              stock['stock'].map(s =>
                <Card key={s.trader_id} bg="light" style={{ minWidth: '25rem', maxWidth: '100rem', margin: '1rem' }}>
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
