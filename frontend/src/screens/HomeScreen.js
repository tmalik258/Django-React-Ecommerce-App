import React, { useState, useEffect } from "react";
import Product from "../components/Product";
import { Col, Row } from "react-bootstrap";
import axios from "axios";

const HomeScreen = () => {
	const [products, setProducts] = useState([]);

    useEffect( () =>
    {
        async function fetchProduct ()
        {
            const { data } = await axios.get( '/api/products' );
            setProducts( data );
        }
        fetchProduct();
    }, [])

	return (
		<div>
			<h1 className="text-uppercase">Latest Inventory</h1>
			<Row>
				{products.map((product) => (
					<Col key={product.id} sm="12" md="6" lg="4" xl="3">
						<Product product={product} />
					</Col>
				))}
			</Row>
		</div>
	);
};

export default HomeScreen;
