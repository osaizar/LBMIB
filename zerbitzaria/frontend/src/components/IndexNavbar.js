import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {connect} from 'react-redux';
import { logoutUser } from '../actions/UserActions';

import {Navbar, Nav, Button} from 'react-bootstrap';
import {FaPlus} from 'react-icons/fa';

class IndexNavbar extends Component {

  constructor(props){
    super(props);

    this.onLogout = this.onLogout.bind(this);
  }

  onLogout(){
    this.props.logoutUser(this.props.user.token)
  }

  render() {
      return (
        <Navbar bg="light" expand="lg" fixed="top">
          <Navbar.Brand>LBMIB</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav"/>
          <Navbar.Collapse className="justify-content-end">
            <Nav className="mr-auto">
              <Navbar.Text>Kaixo, {this.props.user.username}</Navbar.Text>
            </Nav>
            <Nav>
              <Button onClick={this.onLogout} variant="success" className="horizontal-margins"><FaPlus/></Button>
              <Button onClick={this.onLogout} variant="light" className="horizontal-margins">Irten</Button>
            </Nav>
          </Navbar.Collapse>
        </Navbar>
    );
  }
}

IndexNavbar.propTypes = {
  logoutUser : PropTypes.func.isRequired,
  user : PropTypes.object.isRequired
}

const mapStateToProps = state => ({
  user : state.user.user
});


export default connect(mapStateToProps, { logoutUser })(IndexNavbar);
