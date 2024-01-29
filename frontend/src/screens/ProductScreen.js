import React, { useState, useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import { Row, Col, Image, ListGroup, Card, Button } from "react-bootstrap";
import Rating from "../components/Rating";
import axios from "axios";

const ProductScreen = () => {
	const { id } = useParams();
	const [product, setProduct] = useState([]);

	useEffect( () =>
	{
		const getProduct = async () =>
		{
			console.log(id)
			const response = await axios.get( `/api/product/${ id }` );
			setProduct( response.data );
		};

		getProduct();
	}, [id])

	return (
		<div>
			<Link to="/" className="btn btn-light my-3">
				Back to Home
			</Link>
			<Row>
				<Col md={6}>
					<Image
						className="rounded-4"
						src={product.image}
						alt={product.name}
						fluid
					/>
				</Col>

				<Col md={3}>
					<ListGroup variant="flush" className="rounded-3">
						<ListGroup.Item>
							<h3>{product.name}</h3>
						</ListGroup.Item>
						<ListGroup.Item>
							<Rating
								value={product.rating}
								text={`${product.num_reviews} ratings`}
								color={"#f8e825"}
							/>
						</ListGroup.Item>
						<ListGroup.Item>Price: {product.price}</ListGroup.Item>
						<ListGroup.Item>Description: {product.description}</ListGroup.Item>
					</ListGroup>
				</Col>

				<Col md={3}>
					<Card>
						<ListGroup variant="flush" className="rounded-3">
							<ListGroup.Item>
								<Row>
									<Col>Price:</Col>
									<Col>
										<strong>${product.price}</strong>
									</Col>
								</Row>
							</ListGroup.Item>
							<ListGroup.Item>
								<Row>
									<Col>Status:</Col>
									<Col>
										{product.count_in_stock > 0 ? "In Stock" : "Out of Stock"}
									</Col>
								</Row>
							</ListGroup.Item>
							<ListGroup.Item>
								<Button
									className="btn-block"
									disabled={product.count_in_stock > 0 ? false : true}
									type="button"
								>
									Add to Cart
								</Button>
							</ListGroup.Item>
						</ListGroup>
					</Card>
				</Col>
			</Row>
		</div>
	);
};

export default ProductScreen;
