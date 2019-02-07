import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { getUser } from '../actions/UserActions';
import LoginPage from './LoginPage';
import IndexPage from './IndexPage';

class Index extends Component {

  componentWillMount(){
    const token = localStorage.getItem("token");
    if (token != undefined && token != ""){
      this.props.getUser(token);
    }
  }

  render() {
    if (this.props.user.token == ''){
      return (
        <LoginPage/>
      );
    }else{
      return(
        <IndexPage/>
      );
    }
  }
}

Index.propTypes = {
  user : PropTypes.object.isRequired,
  getUser : PropTypes.func.isRequired
}

const mapStateToProps = state => ({
  user : state.user.user
});

export default connect(mapStateToProps, { getUser })(Index);
