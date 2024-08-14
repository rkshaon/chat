// src/store/modules/auth.js

import { login } from "@/services/userAPIService";

const state = {
    accessToken: null,
    refreshToken: null,
};

const mutations = {
    setTokens(state, { accessToken, refreshToken }) {
        state.accessToken = accessToken;
        state.refreshToken = refreshToken;
        localStorage.setItem("accessToken", accessToken);
        localStorage.setItem("refreshToken", refreshToken);
    },
    clearTokens(state) {
        state.accessToken = null;
        state.refreshToken = null;
        localStorage.removeItem("accessToken");
        localStorage.removeItem("refreshToken");
    },
};

const actions = {
    async userLogin({ commit }, credentials) {
        try {
            const response = await login(credentials);
            const { access, refresh } = response.data;

            commit("setTokens", {
                accessToken: access,
                refreshToken: refresh,
            });
            
            return response;
        } catch (error) {
            console.error(
                "Login error:",
                error.response ? error.response.data : error.message
            );
            throw error;
        }
    },
    logout({ commit }) {
        commit("clearTokens");
    },
};

const getters = {
    isAuthenticated: (state) => !!state.accessToken,
    getAccessToken: (state) => state.accessToken,
};

export default {
    namespaced: true,
    state,
    mutations,
    actions,
    getters,
};
