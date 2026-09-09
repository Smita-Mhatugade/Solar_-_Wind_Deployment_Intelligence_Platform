import api from '../services/api';

/**
 * analysisService — Handles communication with the unified FastAPI analysis endpoint.
 */
export const analysisService = {
  /**
   * Run the full end-to-end analysis pipeline.
   * @param {number} latitude 
   * @param {number} longitude 
   * @param {string} siteName 
   * @returns {Promise<Object>} The unified analysis JSON response
   */
  async runAnalysis(latitude, longitude, siteName) {
    const { data } = await api.post('/analysis/', {
      latitude: parseFloat(latitude),
      longitude: parseFloat(longitude),
      site_name: siteName
    });
    return data;
  },

  /**
   * Fetch the user's saved site analyses history.
   * @returns {Promise<Array>} List of saved site analyses.
   */
  async getHistory() {
    try {
      const { data } = await api.get('/analysis/history');
      if (Array.isArray(data)) return data;
      throw new Error('Response is not an array');
    } catch {
      const local = localStorage.getItem('site_analyses');
      try {
        const parsed = local ? JSON.parse(local) : [];
        return Array.isArray(parsed) ? parsed : [];
      } catch {
        return [];
      }
    }
  },

  /**
   * Delete a saved site analysis from history.
   * @param {number} analysisId 
   * @returns {Promise<Object>}
   */
  async deleteHistory(analysisId) {
    try {
      const { data } = await api.delete(`/analysis/history/${analysisId}`);
      return data;
    } catch {
      const local = localStorage.getItem('site_analyses');
      const parsed = local ? JSON.parse(local) : [];
      const filtered = parsed.filter(item => String(item.id) !== String(analysisId));
      localStorage.setItem('site_analyses', JSON.stringify(filtered));
      return { status: 'deleted' };
    }
  }
};
