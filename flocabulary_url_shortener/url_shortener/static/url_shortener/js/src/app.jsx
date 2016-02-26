import React from 'react';

var ShortenUrlForm = React.createClass({
  propTypes: {
    onSubmit: React.PropTypes.func.isRequired
  },

  getInitialState () {
    return { longUrl: '' };
  },

  handleSubmit (event) {
    event.preventDefault();
    this.props.onSubmit(this.state.longUrl);
  },

  handleChange (event) {
    this.setState({ longUrl: event.target.value });
  },

  render () {
    return (
      <form className="shorten-url__form" onSubmit={this.handleSubmit}>
        <input className="shorten-url__input" type="text" value={this.state.longUrl} placeholder="Enter a link to shorten it" onChange={this.handleChange}/>
      </form>
    );
  }
});

export default React.createClass({
  displayName: 'App',

  requestShortUrl (longUrl) {
    var fetchParams = {
      method: 'post',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-CSRFTOKEN': document.cookie.replace(/(?:(?:^|.*;\s*)csrftoken\s*\=\s*([^;]*).*$)|^.*$/, '$1')
      },
      credentials: 'same-origin',
      body: JSON.stringify({ long_url: longUrl })
    };

    fetch('/shorten', fetchParams)
      .then(function (response) {
        if (response.status >= 200 && response.status < 300) {
          return response;
        } else {
          let error = new Error(response.statusText);
          error.response = response;
          throw error;
        }
      })
      .then(response => response.json())
      .then(function ({ short_url: shortUrl, long_url: longUrl }) {
        debugger;
      });
  },

  render () {
    return (
      <div className="shorten-url">
        <ShortenUrlForm onSubmit={this.requestShortUrl}/>
      </div>
    );
  }
});
