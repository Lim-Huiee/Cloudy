import { createStore } from 'vuex';
import { fetch } from '../plugins/fetch';

const store = createStore({
  state () {
    return {
      token: "",
      products: [],
      toastrResponse: {},
      isLoading: false
    }
  },
  getters: {
    isLoading: state => state.isLoading,
    products: state => state.products
  },
  mutations: {
    setProducts(state, products) {
      state.products = products;
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
    async deleteProduct(_, payload) {
      try {
        await fetch({
          method: 'DELETE',
          url: '/delete_product',
          data: payload
        })
        commit('setToastrResponse', {isError: false, msg: 'Product has been deleted!'}, {root: true});
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
        await fetch({
          method: 'POST',
          url: '/create_account',
          data: payload
        })
      } catch (error) {
        console.log(error);
      }
    },
  },
  modules: {},
  plugins: []
})

export default store;