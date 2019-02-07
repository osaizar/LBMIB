import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { loginUser } from '../actions/UserActions';

import { Button, Form, Container, Card} from 'react-bootstrap';

class LoginPage extends Component {

  constructor(props) {
    super(props);
    this.state = {
      username : '',
      password : ''
    }

    this.onChange = this.onChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  onChange(e){
    this.setState({[e.target.name] : e.target.value});
  }

  onSubmit(e){
    e.preventDefault();
    const user = {
      username : this.state.username,
      password : this.state.password
    }

    this.props.loginUser(user);
  }

  render(){
    return(
      <Container>
        <Card>
          <Card.Header as="h3">Sartu</Card.Header>
          <Card.Body>
            <Form id="signInForm" onSubmit={this.submit}>
              <Form.Group>
                <Form.Label>Erabiltzaile izena:</Form.Label>
                <Form.Control type="text" name="username" value={this.state.username} onChange={this.onChange}/>
              </Form.Group>
              <Form.Group>
                <Form.Label>Pasahitza</Form.Label>
                <Form.Control type="password" name="password" value={this.state.password} onChange={this.onChange}/>
              </Form.Group>
              <br/><Button type="submit">Sartu</Button>
            </Form>
          </Card.Body>
        </Card>
      </Container>
    );
  }

}

LoginPage.propTypes = {
  loginUser : PropTypes.func.isRequired
}

export default connect(null, { loginUser })(LoginPage);
