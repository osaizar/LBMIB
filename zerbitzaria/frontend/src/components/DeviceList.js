import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {connect} from 'react-redux';

import { getDevices } from '../actions/DeviceActions';

import {Card, Container, Button, Row, Col, Form} from 'react-bootstrap';

class DeviceList extends Component {

  componentWillMount(){
    this.props.getDevices();
  }

  render() {
    const devices = this.props.devices.map(device => (
      <DeviceListElement title={device.title} text={device.text} key={device.id}/>
    ));

      return (
        <Container>
          {devices}
        </Container>
    );
  }
}

class DeviceListElement extends Component {
  render(){
    return (
      <Card className="horizontal-margins vertical-margins">
        <Card.Body>
          <Card.Title>{this.props.title}</Card.Title>
          <Card.Subtitle className="mb-2 text-muted">Azken aldaketa: 1970-01-01</Card.Subtitle>
          <Row>
            <Col xs="9">
              <Form.Control type="textarea" rows="1" value={this.props.text} readOnly></Form.Control>
            </Col>
            <Col>
              <Button>Aldatu</Button>
            </Col>
            <Col>
              <Button>Aukerak</Button>
            </Col>
          </Row>

        </Card.Body>
      </Card>
    );
  }
}

DeviceList.propTypes = {
  getDevices : PropTypes.func.isRequired,
  devices : PropTypes.array.isRequired
}

const mapStateToProps = state => ({
  devices : state.devices.devices
});

export default connect(mapStateToProps, {getDevices})(DeviceList);
