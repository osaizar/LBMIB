import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { fetchPosts } from '../actions/PostActions';
import {Container, Card} from 'react-bootstrap';

class Posts extends Component {

  componentWillMount(){
    this.props.fetchPosts();
  }

  componentWillReceiveProps(nextProps){
    if (nextProps.newPost){
      this.props.posts.unshift(nextProps.newPost) // like append but at the start
    }
  }

  render() {
    const postItems = this.props.posts.map(post => (
      <Card key={post.id} style={{'margin-top': '1em'}}>
        <Card.Header as="h5">{post.title}</Card.Header>
        <Card.Body>
          <Card.Text>
            {post.body}
          </Card.Text>
        </Card.Body>
      </Card>
    ));

    return (
      <Container style={{'margin-top': '3em'}}>
        <h1> Posts </h1>
        { postItems }
      </Container>
    );
  }
}

Posts.propTypes = {
  fetchPosts : PropTypes.func.isRequired,
  posts : PropTypes.array.isRequired,
  newPost : PropTypes.object
}

const mapStateToProps = state => ({
  posts : state.posts.items,
  newPost : state.posts.item
});

export default connect(mapStateToProps, { fetchPosts })(Posts);
