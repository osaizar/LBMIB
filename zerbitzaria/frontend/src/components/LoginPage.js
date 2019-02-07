import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { Container } from 'react-bootstrap';

import LoginForm from './forms/LoginForm';

class LoginPage extends Component {

  render(){
    return(
      <Container id="loginForm">
        <LoginForm/>
      </Container>
    );
  }
}

LoginPage.propTypes = {

}

export default connect(null, null)(LoginPage);
