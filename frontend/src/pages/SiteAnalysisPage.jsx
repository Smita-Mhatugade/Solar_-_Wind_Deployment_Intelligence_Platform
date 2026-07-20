import { useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';

export default function SiteAnalysisPage() {
  const [formData, setFormData] = useState({
    site_name: '',
    latitude: '',
    longitude: ''
  });
  
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [report, setReport] = useState(null);

  const validateCoordinates = (lat, lon) => {
    if (isNaN(lat) || lat < -90 || lat > 90) return "Latitude must be a number between -90 and 90.";
    if (isNaN(lon) || lon < -180 || lon > 180) return "Longitude must be a number between -180 and 180.";
    return null;
  };

  const handleAnalyze = async (e) => {
    e.preventDefault();
    setError(null);
    setReport(null);

    const lat = parseFloat(formData.latitude);
    const lon = parseFloat(formData.longitude);
    
    // Frontend Validation
    const validationError = validateCoordinates(lat, lon);
    if (validationError) {
      setError(validationError);
      return;
    }

    if (!formData.site_name.trim()) {
      setError("Please provide a site name.");
      return;
    }

    setLoading(true);
    try {
      const response = await api.post('/site/analyze', {
        site_name: formData.site_name,
        latitude: lat,
        longitude: lon
      });
      setReport(response.data);
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.detail || "An error occurred while analyzing the site.");
    } finally {
      setLoading(false);
    }
  };

  const CriteriaCard = ({ title, value, status, unit }) => (
    <div className="card" style={{ padding: '1rem', borderLeft: `4px solid ${status === 'Pass' ? 'var(--color-green)' : 'var(--color-red)'}` }}>
      <div style={{ fontSize: 'var(--font-size-sm)', color: 'var(--text-muted)' }}>{title}</div>
      <div style={{ fontSize: '1.5rem', fontWeight: 700, margin: '0.25rem 0' }}>
        {value} <span style={{ fontSize: 'var(--font-size-sm)', color: 'var(--text-muted)', fontWeight: 400 }}>{unit}</span>
      </div>
      <div className={`badge ${status === 'Pass' ? 'badge-success' : 'badge-user'}`}>{status}</div>
    </div>
  );

  return (
    <div className="page-content">
      <div className="page-header" style={{ marginBottom: '2rem' }}>
        <div>
          <h1 className="page-title">Site Suitability Analysis</h1>
          <p className="page-subtitle">Analyze geographical locations to determine suitability for renewable deployment.</p>
        </div>
      </div>

      <div className="grid-2">
        {/* Input Form */}
        <div className="card">
          <h2 style={{ fontSize: 'var(--font-size-lg)', fontWeight: 700, marginBottom: '1rem' }}>Configuration</h2>
          <form onSubmit={handleAnalyze} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <div>
              <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 600 }}>Site Name</label>
              <input 
                type="text" 
                className="input" 
                placeholder="e.g. Project Alpha Site"
                value={formData.site_name}
                onChange={(e) => setFormData({...formData, site_name: e.target.value})}
                required
              />
            </div>
            
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
              <div>
                <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 600 }}>Latitude</label>
                <input 
                  type="number" 
                  step="any"
                  className="input" 
                  placeholder="-90 to 90"
                  value={formData.latitude}
                  onChange={(e) => setFormData({...formData, latitude: e.target.value})}
                  required
                />
              </div>
              <div>
                <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 600 }}>Longitude</label>
                <input 
                  type="number" 
                  step="any"
                  className="input" 
                  placeholder="-180 to 180"
                  value={formData.longitude}
                  onChange={(e) => setFormData({...formData, longitude: e.target.value})}
                  required
                />
              </div>
            </div>

            {error && (
              <div style={{ padding: '0.75rem', background: 'rgba(239, 68, 68, 0.1)', color: '#ef4444', borderRadius: 'var(--radius-md)' }}>
                {error}
              </div>
            )}

            <button type="submit" className="btn btn-primary" disabled={loading} style={{ marginTop: '1rem' }}>
              {loading ? <span className="spinner" /> : 'Run Analysis'}
            </button>
          </form>
        </div>

        {/* Results Panel */}
        <div>
          {loading && (
            <div className="card" style={{ height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column', color: 'var(--text-muted)' }}>
              <span className="spinner" style={{ width: '40px', height: '40px', marginBottom: '1rem', borderTopColor: 'var(--color-primary)' }} />
              <p>Gathering satellite and vector data...</p>
            </div>
          )}
          
          {!loading && !report && (
            <div className="card empty-state" style={{ height: '100%' }}>
              <h3>Ready to analyze</h3>
              <p>Enter coordinates to fetch the detailed evaluation report.</p>
            </div>
          )}

          {!loading && report && (
            <div className="card" style={{ borderTop: '4px solid var(--color-primary)', animation: 'fadeIn 0.5s ease' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '1.5rem' }}>
                <div>
                  <h2 style={{ fontSize: 'var(--font-size-xl)', fontWeight: 800 }}>Evaluation Report</h2>
                  <p style={{ color: 'var(--text-muted)' }}>Site ID: {report.site_id}</p>
                </div>
                <div style={{ textAlign: 'right' }}>
                  <div style={{ fontSize: '2rem', fontWeight: 800, color: 'var(--color-primary)' }}>{report.overall_score.toFixed(1)} / 100</div>
                  <div className="badge badge-success">{report.recommendation}</div>
                </div>
              </div>

              <h3 style={{ fontSize: 'var(--font-size-md)', fontWeight: 700, marginBottom: '1rem' }}>Criteria Assessment</h3>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1.5rem' }}>
                <CriteriaCard title="Solar Irradiance" value={report.criteria_evaluation.solar_irradiance.value} status={report.criteria_evaluation.solar_irradiance.status} unit="kWh/m²" />
                <CriteriaCard title="Wind Speed" value={report.criteria_evaluation.wind_speed.value} status={report.criteria_evaluation.wind_speed.status} unit="m/s" />
                <CriteriaCard title="Slope" value={report.criteria_evaluation.slope.value} status={report.criteria_evaluation.slope.status} unit="°" />
                <CriteriaCard title="Distance to Grid" value={report.criteria_evaluation.distance_to_grid.value} status={report.criteria_evaluation.distance_to_grid.status} unit="km" />
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
                <div>
                  <h3 style={{ fontSize: 'var(--font-size-md)', fontWeight: 700, marginBottom: '1rem' }}>Constraints</h3>
                  <ul style={{ listStyle: 'none', padding: 0 }}>
                    <li style={{ display: 'flex', justifyContent: 'space-between', padding: '0.5rem 0', borderBottom: '1px solid var(--bg-border)' }}>
                      <span>Protected Area</span>
                      <span>{report.constraints.protected_area ? 'Yes' : 'No'}</span>
                    </li>
                    <li style={{ display: 'flex', justifyContent: 'space-between', padding: '0.5rem 0' }}>
                      <span>Water Body</span>
                      <span>{report.constraints.water_body ? 'Yes' : 'No'}</span>
                    </li>
                  </ul>
                </div>
                
                <div>
                  <h3 style={{ fontSize: 'var(--font-size-md)', fontWeight: 700, marginBottom: '1rem' }}>Remarks</h3>
                  <ul style={{ paddingLeft: '1.25rem', color: 'var(--text-secondary)' }}>
                    {report.remarks.map((remark, idx) => (
                      <li key={idx} style={{ marginBottom: '0.5rem' }}>{remark}</li>
                    ))}
                  </ul>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
