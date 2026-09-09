/**
 * services/api.js — Public Axios Instance & Local Storage Fallback Service
 */
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Graceful error logging (no redirect to login)
    console.warn('API Response Warning:', error.response?.status, error.message);
    return Promise.reject(error);
  }
);

export default api;

export const authService = {
  async login() {
    return { access_token: 'public-access-token', token_type: 'bearer' };
  },
  async register() {
    return { id: 1, email: 'public@platform.local' };
  },
  async getMe() {
    return { id: 1, email: 'public@platform.local', full_name: 'Public User', role: 'analyst' };
  },
  logout() {},
  isAuthenticated() {
    return true;
  },
};

export const projectService = {
  async getAll() {
    try {
      const { data } = await api.get('/projects');
      return data;
    } catch {
      const local = localStorage.getItem('user_projects');
      return local ? JSON.parse(local) : [
        { id: 1, project_name: 'Solar Demo Site A', state: 'Abu Dhabi', latitude: 24.47, longitude: 54.37, description: 'High irradiance solar location' },
        { id: 2, project_name: 'Wind Demo Site B', state: 'Ras Al Khaimah', latitude: 25.67, longitude: 55.98, description: 'High wind class coastal location' }
      ];
    }
  },

  async getById(id) {
    const projects = await this.getAll();
    return projects.find(p => String(p.id) === String(id)) || projects[0];
  },

  async create(payload) {
    try {
      const { data } = await api.post('/projects', payload);
      return data;
    } catch {
      const projects = await this.getAll();
      const newProj = { id: Date.now(), ...payload };
      projects.unshift(newProj);
      localStorage.setItem('user_projects', JSON.stringify(projects));
      return newProj;
    }
  },

  async update(id, payload) {
    const projects = await this.getAll();
    const idx = projects.findIndex(p => String(p.id) === String(id));
    if (idx !== -1) {
      projects[idx] = { ...projects[idx], ...payload };
      localStorage.setItem('user_projects', JSON.stringify(projects));
      return projects[idx];
    }
    return payload;
  },

  async delete(id) {
    const projects = await this.getAll();
    const filtered = projects.filter(p => String(p.id) !== String(id));
    localStorage.setItem('user_projects', JSON.stringify(filtered));
  },
};
