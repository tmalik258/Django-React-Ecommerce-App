import { applyMiddleware } from 'redux';
import { configureStore } from '@reduxjs/toolkit';
import { thunk } from 'redux-thunk';
import { productListReducers } from './reducers/productReducer';

const middleware = [thunk]

export default configureStore( {
    reducer: {
        productList: productListReducers
    },
    initialState: {},
    composeWithDevTools: applyMiddleware(...middleware)
})