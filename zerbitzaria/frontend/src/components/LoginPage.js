import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import LoginForm from './forms/LoginForm';

class LoginPage extends Component {

  render(){
    return(
      <LoginForm/>
    );
  }
}

LoginPage.propTypes = {

}

export default connect(null, null)(LoginPage);
