import React from 'react'
import Rating from './Rating';
import { Card } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const Product = ({ product }) => {
  return (
		<Card className="my-3 py-3 rounded-3 shadow">
			<Link to={`/product/${product.id}`} className='px-3'>
				<Card.Img src={product.image} />
			</Link>
			<Card.Body>
				<Link to={`/product/${product.id}`}>
					<Card.Title as="div">
						<strong>{product.name}</strong>
					</Card.Title>
				</Link>
				<Card.Text as="div">
					<div className="my-3">
                      <Rating value={product.rating} text={`${product.num_reviews} reviews`} color={'#f8e825'} />
					</div>
              </Card.Text>
              <Card.Text as="h3">
                  ${product.price}
              </Card.Text>
			</Card.Body>
		</Card>
	);
}

export default Product