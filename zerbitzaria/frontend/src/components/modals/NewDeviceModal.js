import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import { Button, Form, Modal} from 'react-bootstrap';

class NewDeviceModal extends Component {

  constructor(props, context) {
    super(props, context);

    this.state = {
      show: false,
      option : "id",
      pin : "",
      name : ""
    };

    this.nextOption = this.nextOption.bind(this);
    this.onChange = this.onChange.bind(this);
    this.handleShow = this.handleShow.bind(this);
    this.handleClose = this.handleClose.bind(this);
  }

  componentWillRender(){
    if (this.props.show){
      this.handleShow();
    }
  }

  handleShow(){
    this.setState({show : true});
  }

  handleClose(){
    this.setState({show : false});
  }

  nextOption(){
    switch (this.state.option) {
      case "id":
        this.setState({option : "name"});
        break;
      case "name":
        this.setState({option : "okey"});
        break;
      case "okey":
        this.handleClose();
        break;
      default:
        this.setState({option : "id"});
    }
  }

  onChange(e){
    this.setState({[e.target.name] : e.target.value});
  }

  render() {
    var inner;
    if (this.state.option == "id"){
      inner = (
        <Modal.Body>
          <Form.Group>
            <Form.Label>PIN zenbakia sartu:</Form.Label>
            <Form.Control type="text" value={this.state.pin} onChange={this.onChange} name="pin"></Form.Control>
          </Form.Group>
        </Modal.Body>
      );
    }else if (this.state.option == "name") {
      inner = (
       <Modal.Body>
         <Form.Group>
           <Form.Label>Izena:</Form.Label>
           <Form.Control type="text" value={this.state.name} onChange={this.onChange} name="name"></Form.Control>
         </Form.Group>
       </Modal.Body>
     );
   }else if (this.state.option == "okey"){
     inner = (
       <Modal.Body>
         Dena ondo!
       </Modal.Body>
     );
   }else{
     inner = (<div></div>);
   }

    return (
        <Modal show={this.state.show} onHide={this.handleClose}>
          <Modal.Header closeButton>
            <Modal.Title>Pantaila berria gehitu</Modal.Title>
          </Modal.Header>
          { inner }
          <Modal.Footer>
            <Button variant="success" onClick={this.nextOption}>
              Jarraitu
            </Button>
          </Modal.Footer>
        </Modal>
    );
  }

}

NewDeviceModal.propTypes = {

}

export default connect(null, null)(NewDeviceModal);
