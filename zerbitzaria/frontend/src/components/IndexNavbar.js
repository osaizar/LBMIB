import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {connect} from 'react-redux';
import { logoutUser } from '../actions/UserActions';

import {Navbar, Nav, Button} from 'react-bootstrap';

class IndexNavbar extends Component {

  constructor(props){
    super(props);

    this.onLogout = this.onLogout.bind(this);
  }

  onLogout(){
    this.props.logoutUser(localStorage.getItem("token"))
  }

  render() {
      return (
        <Navbar bg="light" expand="lg">
          <Navbar.Brand>Logoa/Izena</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav"/>
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
              <Nav.Link href="#testeo">Testeo</Nav.Link>
            </Nav>
            <Nav className="navbar-right">
              <Button onClick={this.onLogout} variant="light">Irten</Button>
            </Nav>
          </Navbar.Collapse>
        </Navbar>
    );
  }
}

IndexNavbar.propTypes = {
  logoutUser : PropTypes.func.isRequired
}

const mapStateToProps = state => ({});

export default connect(mapStateToProps, { logoutUser })(IndexNavbar);
