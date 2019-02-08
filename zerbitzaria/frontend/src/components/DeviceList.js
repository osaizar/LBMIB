import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {connect} from 'react-redux';

class DeviceList extends Component {

  render() {
      return (
        <h3>Device List</h3>
    );
  }
}

DeviceList.propTypes = {}

const mapStateToProps = state => ({});

export default connect(mapStateToProps, null)(DeviceList);
