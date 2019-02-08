import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { loginUser } from '../../actions/UserActions';

import { Button, Form, Container, Card} from 'react-bootstrap';

class LoginForm extends Component {

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
        <Card>
          <Card.Header as="h5">Ongietorri</Card.Header>
          <Card.Body>
            <Form id="signInForm" onSubmit={this.onSubmit}>
              <Form.Group>
                <Form.Label>Erabiltzaile izena:</Form.Label>
                <Form.Control type="text" name="username" value={this.state.username} onChange={this.onChange}/>
              </Form.Group>
              <Form.Group>
                <Form.Label>Pasahitza</Form.Label>
                <Form.Control type="password" name="password" value={this.state.password} onChange={this.onChange}/>
              </Form.Group>
              <Button className="pull-right" type="submit" variant="light">Sartu</Button>
            </Form>
          </Card.Body>
        </Card>
    );
  }

}

LoginForm.propTypes = {
  loginUser : PropTypes.func.isRequired
}

export default connect(null, { loginUser })(LoginForm);
