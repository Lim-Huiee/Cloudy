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
        
        return products
      } catch (error) {
        console.log(error);
      }
    },
  },
  modules: {},
  plugins: []
})

export default store;