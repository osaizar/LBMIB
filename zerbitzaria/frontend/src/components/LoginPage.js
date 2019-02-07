import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

class LoginPage extends Component {

  render() {
    return(
      <h1>Login Please</h1>
    );
  }
}

LoginPage.propTypes = {

}

const mapStateToProps = state => ({

});

export default connect(mapStateToProps, null)(LoginPage);
