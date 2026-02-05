/* Main JavaScript for Portal with RTL Support */

document.addEventListener('DOMContentLoaded', function() {
    console.log('Portal initialized - RTL ready');
    
    // Detect RTL language
    const htmlElement = document.documentElement;
    const isRTL = htmlElement.getAttribute('dir') === 'rtl' || htmlElement.lang.startsWith('fa') || htmlElement.lang.startsWith('ar');
    
    // Add fade-in animation on load
    const cards = document.querySelectorAll('.card, .feature-card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.classList.add('fade-in');
        }, index * 100);
    });
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
    
    // Add active class to navbar links based on current page
    const currentLocation = location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav a');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentLocation) {
            link.classList.add('active');
        }
    });
    
    // RTL-aware scroll behavior
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
    
    // Add RTL class to body if needed
    if (isRTL) {
        document.body.classList.add('rtl-mode');
    }
    
    console.log('RTL Support:', isRTL ? 'Enabled (فارسی)' : 'Disabled');
});

// Function to format date in Persian
function formatPersianDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    const formatter = new Intl.DateTimeFormat('fa-IR', options);
    return formatter.format(new Date(date));
}
