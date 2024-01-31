export const productListReducers = ( state = { products: [] }, action ) =>
{
    switch (action.type) {
        case 'PRODUCT_LIST_REQUEST':
            return { loading: true, products: []}
    
        case 'PRODUCT_LIST_SUCCESS':
            return { loading: false, products: action.payload }
        
        case 'PRODUCT_LIST_FAIL': 
        // case 'CREATE_NEW_PRODUCT_FAIL':  
        // case 'UPDATE_PRODUCT_FAIL':  
        // case 'DELETE_PRODUCT_FAIL': 
            return { loading: false, error: action.payload }
        
        default:
            return state;
    }
}