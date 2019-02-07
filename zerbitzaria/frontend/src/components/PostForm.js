import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { newPost } from '../actions/PostActions';

import { Button, Form, Container } from 'react-bootstrap';

class PostForm extends Component {
  constructor(props){
    super(props);

    this.state ={
      title : '',
      body : ''
    };

    this.onChange = this.onChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  onChange(e){
    this.setState({[e.target.name] : e.target.value});
  }

  onSubmit(e){
    e.preventDefault();
    const post = {
      title : this.state.title,
      body : this.state.body
    }

    this.props.newPost(post);
    this.setState({title : '', body : ''})
  }

  render() {
    return (
      <Container>
        <h1> Add Post </h1>
        <Form onSubmit={this.onSubmit}>
          <Form.Group>
            <Form.Label>Title: </Form.Label>
            <Form.Control type="text" name="title" value={this.state.title} onChange={this.onChange}></Form.Control>
          </Form.Group>
          <Form.Group>
            <Form.Label>Body: </Form.Label>
            <Form.Control as="textarea" rows="2" name="body" value={this.state.body} onChange={this.onChange}></Form.Control>
          </Form.Group>
          <Button type="submit">Submit</Button>
        </Form>
      </Container>
    );
  }
}

PostForm.propTypes = {
  newPost : PropTypes.func.isRequired
}

export default connect(null, { newPost })(PostForm);
