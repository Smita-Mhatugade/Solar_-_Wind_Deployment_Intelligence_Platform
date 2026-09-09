/**
 * DashboardPage.jsx — Main overview after login (Public Tool Mode)
 */
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { projectService } from '../services/api';

const QUICK_ACTIONS = [
  { to: '/projects', label: 'New Project', color: 'solar', desc: 'Start a deployment project' },
  { to: '/site-analysis', label: 'Site Suitability', color: 'solar', desc: 'Score a site 0–100' },
];

const DATASET_STATUS = [
  { name: 'NASA POWER', rows: '6,651', cols: 53, status: 'ready', purpose: 'Solar irradiance & climate data' },
  { name: 'Global Wind Atlas', rows: '3 (sample)', cols: 4, status: 'pending', purpose: 'Wind speed at 50m/100m AGL' },
  { name: 'SRTM Elevation', rows: '3 (sample)', cols: 4, status: 'pending', purpose: 'Terrain elevation & slope' },
  { name: 'OpenStreetMap', rows: '3 (sample)', cols: 4, status: 'pending', purpose: 'Road & grid infrastructure' },
  { name: 'Copernicus Sentinel', rows: '3 (sample)', cols: 4, status: 'pending', purpose: 'Land cover & NDVI analysis' },
];

export default function DashboardPage() {
  const [projects, setProjects] = useState([]);
  const [loadingProjects, setLoadingProjects] = useState(true);

  useEffect(() => {
    projectService.getAll()
      .then(res => setProjects(Array.isArray(res) ? res : []))
      .catch(() => setProjects([]))
      .finally(() => setLoadingProjects(false));
  }, []);

  const greeting = new Date().getHours() < 12 ? 'Good morning' : new Date().getHours() < 17 ? 'Good afternoon' : 'Good evening';

  const safeProjects = Array.isArray(projects) ? projects : [];

  return (
    <div className="page-content">
      {/* Welcome header */}
      <div style={{ marginBottom: '2rem' }}>
        <h1 className="page-title">
          {greeting}, Analyst
        </h1>
        <p className="page-subtitle">
          Welcome to the Solar & Wind Deployment Intelligence Platform
        </p>
      </div>

      {/* Stats */}
      <div className="stats-grid" style={{ marginBottom: '2rem' }}>
        <div className="stat-card solar">
          <div className="stat-value" style={{ color: 'var(--color-solar)' }}>
            {loadingProjects ? '…' : safeProjects.length}
          </div>
          <div className="stat-label">My Projects</div>
        </div>

        <div className="stat-card wind">
          <div className="stat-value" style={{ color: 'var(--color-wind)' }}>1</div>
          <div className="stat-label">Active Datasets</div>
        </div>

        <div className="stat-card green">
          <div className="stat-value" style={{ color: 'var(--color-green)' }}>6,651</div>
          <div className="stat-label">NASA POWER Records</div>
        </div>

        <div className="stat-card purple">
          <div className="stat-value" style={{ color: '#a855f7' }}>0</div>
          <div className="stat-label">Reports Generated</div>
        </div>
      </div>

      {/* Main grid */}
      <div className="grid-2" style={{ marginBottom: '2rem' }}>
        {/* Quick Actions */}
        <div className="card">
          <h2 style={{ fontSize: 'var(--font-size-lg)', fontWeight: 700, marginBottom: '1.25rem' }}>
            Quick Actions
          </h2>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            {QUICK_ACTIONS.map((action) => (
              <Link key={action.to} to={action.to} style={{ textDecoration: 'none' }}>
                <div
                  className="card"
                  style={{
                    padding: '0.875rem 1rem',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.875rem',
                    cursor: 'pointer',
                    borderColor: 'var(--bg-border)',
                  }}
                >
                  <div>
                    <div style={{ fontWeight: 600, fontSize: 'var(--font-size-sm)' }}>{action.label}</div>
                    <div style={{ fontSize: 'var(--font-size-xs)', color: 'var(--text-muted)' }}>{action.desc}</div>
                  </div>
                  <span style={{ marginLeft: 'auto', color: 'var(--text-muted)' }}>→</span>
                </div>
              </Link>
            ))}
          </div>
        </div>

        {/* Recent Projects */}
        <div className="card">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.25rem' }}>
            <h2 style={{ fontSize: 'var(--font-size-lg)', fontWeight: 700 }}>Recent Projects</h2>
            <Link to="/projects" className="btn btn-ghost btn-sm">View all →</Link>
          </div>

          {loadingProjects ? (
            <div style={{ textAlign: 'center', padding: '2rem', color: 'var(--text-muted)' }}>
              <span className="spinner" /> Loading…
            </div>
          ) : safeProjects.length === 0 ? (
            <div className="empty-state" style={{ padding: '2rem' }}>
              <h3>No projects yet</h3>
              <p>Create your first solar or wind deployment project</p>
              <Link to="/projects" className="btn btn-primary btn-sm">Create Project</Link>
            </div>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
              {safeProjects.slice(0, 4).map((p) => (
                <div key={p.id || p.project_name} style={{
                  display: 'flex', alignItems: 'center', justifyContent: 'space-between',
                  padding: '0.75rem', background: 'var(--bg-600)', borderRadius: 'var(--radius-md)',
                }}>
                  <div>
                    <div style={{ fontWeight: 600, fontSize: 'var(--font-size-sm)' }}>{p.project_name || 'Unnamed Project'}</div>
                    <div style={{ fontSize: 'var(--font-size-xs)', color: 'var(--text-muted)' }}>
                      {p.state || 'Region'} · {Number(p.latitude || 0).toFixed(2)}°, {Number(p.longitude || 0).toFixed(2)}°
                    </div>
                  </div>
                  <span className="badge badge-success">Active</span>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* Dataset status */}
      <div className="card">
        <h2 style={{ fontSize: 'var(--font-size-lg)', fontWeight: 700, marginBottom: '1.25rem' }}>
          Dataset Integration Status
        </h2>
        <div className="table-wrapper">
          <table className="data-table">
            <thead>
              <tr>
                <th>Dataset</th>
                <th>Purpose</th>
                <th>Records</th>
                <th>Columns</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {DATASET_STATUS.map((d) => (
                <tr key={d.name}>
                  <td><strong>{d.name}</strong></td>
                  <td style={{ color: 'var(--text-secondary)' }}>{d.purpose}</td>
                  <td>{d.rows}</td>
                  <td>{d.cols}</td>
                  <td>
                    <span className={`badge ${d.status === 'ready' ? 'badge-success' : 'badge-user'}`}>
                      {d.status === 'ready' ? 'Ready' : 'Sample'}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
