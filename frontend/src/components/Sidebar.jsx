/**
 * Sidebar.jsx — Dashboard navigation sidebar (Public Tool Mode)
 */
import { NavLink } from 'react-router-dom';

const NAV_ITEMS = [
  {
    section: 'Overview',
    items: [
      { to: '/dashboard', label: 'Dashboard' },
      { to: '/projects', label: 'My Projects' },
    ],
  },
  {
    section: 'Analysis',
    items: [
      { to: '/site-analysis', label: 'Site Analysis' },
    ],
  },
  {
    section: 'Reports',
    items: [
      { to: '/reports', label: 'Reports' },
    ],
  },
];

export default function Sidebar() {
  return (
    <aside className="sidebar">
      {/* Logo */}
      <div className="sidebar-logo">
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <div>
            <div className="logo-text">Solar & Wind</div>
            <div className="logo-sub">Intelligence Platform</div>
          </div>
        </div>
      </div>

      {/* Nav */}
      <nav className="sidebar-nav">
        {NAV_ITEMS.map((group) => (
          <div key={group.section}>
            <div className="sidebar-section-label">{group.section}</div>
            {group.items.map((item) => (
              <NavLink
                key={item.to}
                to={item.to}
                className={({ isActive }) => `nav-item${isActive ? ' active' : ''}`}
              >
                <span>{item.label}</span>
              </NavLink>
            ))}
          </div>
        ))}
      </nav>

      {/* Footer */}
      <div className="sidebar-footer">
        <div className="user-profile">
          <div className="user-avatar">PA</div>
          <div className="user-info">
            <div className="user-name">Public Analyst</div>
            <div className="user-role">Open Access</div>
          </div>
        </div>
      </div>
    </aside>
  );
}
