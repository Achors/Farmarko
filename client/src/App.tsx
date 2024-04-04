import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import ProductList from './components/ProductList';
import ProductDetail from './components/ProductDetail';
import ShoppingCart from './components/ShoppingCart';

function App() {
  return (
    <div className="App">
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/products" component={ProductList} />
        <Route path="/products/:id" component={ProductDetail} />
        <Route path="/cart" component={ShoppingCart} />
      </Switch>
    </div>
  );
}

export default App;
