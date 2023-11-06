import { createStore } from 'vuex';
import { fetch } from '../plugins/fetch';

const store = createStore({
  state () {
    return {
      token: "",
      products: [],
      orders:[],
      toastrResponse: {},
      isLoading: false
    }
  },
  getters: {
    isLoading: state => state.isLoading,
    products: state => state.products,
    orders: state => state.orders

  },
  mutations: {
    setProducts(state, products) {
      state.products = products;
    },
    setOrders(state, orders) {
      state.orders = orders;
    },
    setLoader(state, isLoading) {
      state.isLoading = isLoading;
    }
  },
  actions: {
    async getAllProducts({commit}) {
      try { 
        commit('setLoader', true);
        const {data: {data: products}} = await fetch({
          method: 'GET',
          url: 'product_list'
        })
        
        commit('setProducts', products);
        commit('setLoader', false);
        
      } catch (error) {
        console.log(error);
      }
    },
    async createProduct(_,payload) {
      try { 
        await fetch({
          method: 'POST',
          url: '/create_product',
          data: payload
        })
      } catch (error) {
        console.log(error);
      }
    },
    async updateProduct(_,payload) {
      try {
        let res = await fetch({
          method: 'PUT',
          url: '/update_product',
          data: payload
        })
        return res.data;
      } catch(error) {
        console.log(error);
      }
    },
    async deleteProduct(_, payload) {
      try {
        let res = await fetch({
          method: 'DELETE',
          url: '/delete_product',
          data: payload
        })
        return res.data;
        // commit('setToastrResponse', {isError: false, msg: 'Product has been deleted!'}, {root: true});
      } catch (error) {
          console.log(error);
      }
    },
    async getAllUser({commit}) {
      try { 
        commit('setLoader', true);
        const {data: {data: products}} = await fetch({
          method: 'GET',
          url: 'product_list'
        })
        
        commit('setProducts', products);
        commit('setLoader', false);
        
      } catch (error) {
        console.log(error);
      }
    },
    async createUserAccount(_,payload) {
      try { 
        let res = await fetch({
          method: 'POST',
          url: '/create_account',
          data: payload
        })
        return res.data;
      } catch (error) {
        console.log(error);
      }
    },
    async logIn(_,payload) {
      try {
        let res = await fetch({
          method: 'POST',
          url: '/login',
          data: payload
        })
        return res.data;
      } catch(error) {
        console.log(error);
      }
    },
    async getAllOrders({commit}) {
      try { 
        commit('setLoader', true);
        const {data: {data: orders}} = await fetch({
          method: 'GET',
          url: 'order_list'
        })
        
        commit('setOrders', orders);
        commit('setLoader', false);
      } catch (error) {
        console.log(error);
      }
    },
    async createOrder(_,payload) {
      try {
        let res = await fetch({
          method: 'POST',
          url: '/create_order',
          data: payload
        })
        return res.data;
      } catch(error) {
        console.log(error);
      }
    },
    async updateOrder(_,payload) {
      try {
        let res = await fetch({
          method: 'PUT',
          url: '/update_order',
          data: payload
        })
        return res.data;
      } catch(error) {
        console.log(error);
      }
    },
  },
  modules: {},
  plugins: []
})

export default store;