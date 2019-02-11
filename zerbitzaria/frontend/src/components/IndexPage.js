import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {connect} from 'react-redux';

import { Card, Container } from 'react-bootstrap';

import DeviceList from './DeviceList';
import IndexNavbar from './IndexNavbar';

class IndexPage extends Component {

  render() {
      return (
        <div>
          <IndexNavbar/>
          <Container className="page-center">
            <DeviceList/>
          </Container>
        </div>
    );
  }
}

IndexPage.propTypes = {}

const mapStateToProps = state => ({});

export default connect(mapStateToProps, null)(IndexPage);
