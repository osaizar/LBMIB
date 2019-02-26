import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {connect} from 'react-redux';

import {Button, Form, Modal} from 'react-bootstrap';

class NewDeviceModal extends Component {

  constructor(props, context) {
    super(props, context);

    this.state = {
      option: "id",
      pin: "",
      name: ""
    };

    this.nextOption = this.nextOption.bind(this);
    this.onChange = this.onChange.bind(this);
    this.finish = this.finish.bind(this);
    this.send = this.send.bind(this);
  }

  send() {
    //TODO: Send data to server
    //TODO: change state to correct or not
  }

  finish() {
    this.setState({pin: "", name: ""})
    this.props.toggle();
  }

  nextOption() {
    switch (this.state.option) {
      case "id":
        this.setState({option: "name"});
        break;
      case "name":
        this.send();
        this.setState({option: "waiting"});
        break;
      case "error":
        this.setState({option: "id"});
        break;
      case "okey":
        this.finish();
        break;
      case "waiting":
        break;
      default:
        this.setState({option: "id"});
    }
  }

  onChange(e) {
    this.setState({
      [e.target.name]: e.target.value
    });
  }

  render() {
    var inner;
    //TODO: add gifs and images
    if (this.state.option == "id") {
      inner = (
        <Modal.Body>
          <Form.Group>
            <Form.Label>PIN zenbakia sartu:</Form.Label>
            <Form.Control type="text" value={this.state.pin} onChange={this.onChange} name="pin"></Form.Control>
          </Form.Group>
        </Modal.Body>
      );
    } else if (this.state.option == "name") {
      inner = (
        <Modal.Body>
          <Form.Group>
            <Form.Label>Izena:</Form.Label>
            <Form.Control type="text" value={this.state.name} onChange={this.onChange} name="name"></Form.Control>
          </Form.Group>
        </Modal.Body>        <Modal.Body>
          Dena ondo!
        </Modal.Body>
      );
    } else if (this.state.option == "okey") {
      inner = (
        <Modal.Body>
          Dena ondo!
        </Modal.Body>
      );
    } else if (this.state.option == "error") {
      inner = (
        <Modal.Body>
          Errore bat gertatu da...
        </Modal.Body>
      );
    } else if (this.state.option == "waiting") {
      inner = (
        <Modal.Body>
          itxaroten...
        </Modal.Body>
      );
    } else {
      inner = (<div></div>);
    }

    return (
      <Modal show={this.props.show} onHide={this.props.toggle}>
        <Modal.Header closeButton="closeButton">
          <Modal.Title>Pantaila berria gehitu</Modal.Title>
        </Modal.Header>
        {inner}
        <Modal.Footer>
          <Button variant="success" onClick={this.nextOption}>
            Jarraitu
          </Button>
        </Modal.Footer>
      </Modal>
    );
  }
}

export default connect(null, null)(NewDeviceModal);
