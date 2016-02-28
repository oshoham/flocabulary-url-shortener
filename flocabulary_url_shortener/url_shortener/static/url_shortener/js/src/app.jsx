import React from 'react';
import Clipboard from 'clipboard';

export default React.createClass({
  getInitialState () {
    return {
      longUrl: '',
      shortUrl: '',
      hasShortUrl: false,
      displayShortUrl: false,
      copyOnSubmit: false
    };
  },

  componentDidUpdate () {
    if (this.state.copyOnSubmit) {
      this.clipboard = new Clipboard('.shorten-url__submit', { text: () => this.state.shortUrl });
    } else if (this.clipboard) {
      this.clipboard.destroy();
    }
  },

  handleInputChange (event) {
    var value = event.target.value;
    this.setState({
      longUrl: value,
      displayShortUrl: false,
      copyOnSubmit: this.state.hasShortUrl && value === this.state.shortUrl
    });
  },

  handleFormSubmit (event) {
    event.preventDefault();

    if (!this.state.displayShortUrl && this.state.longUrl) {
      this.fetchShortUrl(this.state.longUrl).then(({ short_url, long_url }) => {
        this.setState({
          shortUrl: short_url,
          longUrl: long_url,
          hasShortUrl: true,
          displayShortUrl: true,
          copyOnSubmit: true
        });
      });
    }
  },

  fetchShortUrl (longUrl) {
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

    return fetch('/shorten', fetchParams)
      .then(function (response) {
        if (response.status >= 200 && response.status < 300) {
          return response;
        } else {
          let error = new Error(response.statusText);
          error.response = response;
          throw error;
        }
      })
      .then(response => response.json());
  },

  clearInput (event) {
    event.preventDefault();
    this.setState({
      longUrl: '',
      displayShortUrl: false,
      copyOnSubmit: false
    });
  },

  render () {
    var inputValue = this.state.displayShortUrl ? this.state.shortUrl : this.state.longUrl;
    var buttonValue = this.state.copyOnSubmit ? 'Copy' : 'Shorten';
    var clearInputLink = this.state.displayShortUrl ? <a href="#" className="shorten-url__clear" onClick={this.clearInput}>X</a> : null;

    return (
      <div className="shorten-url">
        <form className="shorten-url__form" onSubmit={this.handleFormSubmit}>
          <fieldset className="shorten-url__fieldset">
            <input className="shorten-url__input" type="text" value={inputValue} placeholder="Enter a link to shorten it" onChange={this.handleInputChange}/>
            {clearInputLink}
            <button className="shorten-url__submit" type="submit">{buttonValue}</button>
          </fieldset>
        </form>
      </div>
    );
  }
});
