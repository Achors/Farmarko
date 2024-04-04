import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Product {
  id: number;
  name: string;
  price: number;
}

const ProductList: React.FC = () => {
  const [products, setProducts] = useState<Product[]>([]);

  useEffect(() => {
    axios.get('/api/products')
      .then(response => setProducts(response.data))
      .catch(error => console.error('Error fetching products:', error));
  }, []);

  return (
    <div>
      <h2>Products</h2>
      <ul>
        {products.map(product => (
          <li key={product.id}>
            <p>{product.name}</p>
            <p>${product.price}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ProductList;
