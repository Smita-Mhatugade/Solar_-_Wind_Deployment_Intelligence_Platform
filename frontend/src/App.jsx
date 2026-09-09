/**
 * App.jsx — Main application with React Router & ErrorBoundary (Public Tool Mode)
 */
import { BrowserRouter, Routes, Route, Navigate, useLocation } from 'react-router-dom';
import './App.css';

import ErrorBoundary from './components/ErrorBoundary';
import Sidebar from './components/Sidebar';
import DashboardPage from './pages/DashboardPage';
import ProjectsPage from './pages/ProjectsPage';
import SiteAnalysisPage from './pages/SiteAnalysisPage';
import ReportsPage from './pages/ReportsPage';

/** Layout wrapper: sidebar + topbar + content */
function DashboardLayout({ children }) {
  const location = useLocation();

  const TITLES = {
    '/dashboard': { label: 'Dashboard' },
    '/projects': { label: 'My Projects' },
    '/site-analysis': { label: 'Site Suitability Analysis' },
    '/reports': { label: 'Reports' },
  };

  const current = TITLES[location.pathname] || { label: 'Platform' };

  return (
    <div className="app-layout">
      <Sidebar />
      <div className="main-content">
        {/* Topbar */}
        <header className="topbar">
          <div className="topbar-title">
            {current.label}
          </div>
          <div className="topbar-actions">
            <span className="badge badge-success">Public Intelligence Tool</span>
          </div>
        </header>
        {children}
      </div>
    </div>
  );
}

export default function App() {
  return (
    <ErrorBoundary>
      <BrowserRouter>
        <Routes>
          <Route
            path="/dashboard"
            element={
              <DashboardLayout>
                <DashboardPage />
              </DashboardLayout>
            }
          />
          <Route
            path="/projects"
            element={
              <DashboardLayout>
                <ProjectsPage />
              </DashboardLayout>
            }
          />
          <Route
            path="/site-analysis"
            element={
              <DashboardLayout>
                <SiteAnalysisPage />
              </DashboardLayout>
            }
          />
          <Route
            path="/reports"
            element={
              <DashboardLayout>
                <ReportsPage />
              </DashboardLayout>
            }
          />

          {/* Default redirects */}
          <Route path="/" element={<Navigate to="/dashboard" replace />} />
          <Route path="*" element={<Navigate to="/dashboard" replace />} />
        </Routes>
      </BrowserRouter>
    </ErrorBoundary>
  );
}
