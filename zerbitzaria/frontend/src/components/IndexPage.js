import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

class IndexPage extends Component {

  render() {
    return(
      <h1>Index Page</h1>
    );
  }
}

IndexPage.propTypes = {

}

const mapStateToProps = state => ({

});

export default connect(mapStateToProps, null)(IndexPage);
