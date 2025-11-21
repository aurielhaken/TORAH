// =============================================
// DOCTHAIR - PREMIUM LANDING PAGE 2025
// Interactive JavaScript
// =============================================

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
    initMobileMenu();
    initScrollAnimations();
    initParticles();
    initCTAButtons();
    initVideoFallback();
    initSmoothScroll();
});

// =============================================
// NAVBAR SCROLL EFFECT
// =============================================
function initNavbar() {
    const navbar = document.getElementById('navbar');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        // Add scrolled class when scrolled down
        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
    });
}

// =============================================
// MOBILE MENU
// =============================================
function initMobileMenu() {
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const navLinks = document.getElementById('navLinks');
    const body = document.body;

    if (!mobileMenuBtn || !navLinks) return;

    mobileMenuBtn.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        mobileMenuBtn.classList.toggle('active');
        body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
    });

    // Close menu when clicking on a link
    const links = navLinks.querySelectorAll('a');
    links.forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            mobileMenuBtn.classList.remove('active');
            body.style.overflow = '';
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!navLinks.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
            navLinks.classList.remove('active');
            mobileMenuBtn.classList.remove('active');
            body.style.overflow = '';
        }
    });
}

// =============================================
// SCROLL ANIMATIONS (AOS Alternative)
// =============================================
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe all elements with data-aos attribute
    const animatedElements = document.querySelectorAll('[data-aos]');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';

        // Add delay if specified
        const delay = el.getAttribute('data-aos-delay');
        if (delay) {
            el.style.transitionDelay = `${delay}ms`;
        }

        observer.observe(el);
    });
}

// =============================================
// PARTICLES BACKGROUND
// =============================================
function initParticles() {
    const particlesContainer = document.getElementById('particles');
    if (!particlesContainer) return;

    const particleCount = window.innerWidth < 768 ? 30 : 50;

    for (let i = 0; i < particleCount; i++) {
        createParticle(particlesContainer);
    }
}

function createParticle(container) {
    const particle = document.createElement('div');

    const size = Math.random() * 4 + 1;
    const startX = Math.random() * window.innerWidth;
    const startY = Math.random() * window.innerHeight;
    const duration = Math.random() * 20 + 10;
    const delay = Math.random() * 5;

    particle.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        background: radial-gradient(circle, rgba(232, 119, 34, 0.6), transparent);
        border-radius: 50%;
        left: ${startX}px;
        top: ${startY}px;
        pointer-events: none;
        animation: float-particle ${duration}s infinite ease-in-out;
        animation-delay: ${delay}s;
    `;

    container.appendChild(particle);
}

// Add float animation dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes float-particle {
        0%, 100% {
            transform: translate(0, 0);
            opacity: 0.3;
        }
        25% {
            transform: translate(20px, -20px);
            opacity: 0.6;
        }
        50% {
            transform: translate(-10px, -40px);
            opacity: 0.3;
        }
        75% {
            transform: translate(-30px, -20px);
            opacity: 0.6;
        }
    }
`;
document.head.appendChild(style);

// =============================================
// CTA BUTTONS INTERACTIONS
// =============================================
function initCTAButtons() {
    // Primary CTA - Diagnostic
    const primaryCTA = document.querySelector('.btn-cta-primary');
    if (primaryCTA) {
        primaryCTA.addEventListener('click', () => {
            // Add ripple effect
            createRipple(primaryCTA, event);

            // Simulate action (replace with actual navigation)
            setTimeout(() => {
                console.log('Starting diagnostic process...');
                // window.location.href = '/diagnostic';
            }, 300);
        });
    }

    // Secondary CTA - View Report Example
    const secondaryCTA = document.querySelector('.btn-cta-secondary');
    if (secondaryCTA) {
        secondaryCTA.addEventListener('click', () => {
            createRipple(secondaryCTA, event);

            setTimeout(() => {
                console.log('Opening report example...');
                // window.location.href = '/exemple-rapport';
            }, 300);
        });
    }
}

function createRipple(button, event) {
    const ripple = document.createElement('span');
    const rect = button.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = event.clientX - rect.left - size / 2;
    const y = event.clientY - rect.top - size / 2;

    ripple.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.5);
        left: ${x}px;
        top: ${y}px;
        pointer-events: none;
        animation: ripple-effect 0.6s ease-out;
    `;

    button.style.position = 'relative';
    button.style.overflow = 'hidden';
    button.appendChild(ripple);

    setTimeout(() => ripple.remove(), 600);
}

// Add ripple animation
const rippleStyle = document.createElement('style');
rippleStyle.textContent = `
    @keyframes ripple-effect {
        from {
            transform: scale(0);
            opacity: 1;
        }
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(rippleStyle);

// =============================================
// VIDEO FALLBACK
// =============================================
function initVideoFallback() {
    const video = document.querySelector('.background-video');
    const placeholder = document.querySelector('.video-placeholder');

    if (!video || !placeholder) return;

    // Check if video can be played
    video.addEventListener('loadeddata', () => {
        // Hide placeholder once video is loaded
        setTimeout(() => {
            placeholder.style.opacity = '0';
            setTimeout(() => {
                placeholder.style.display = 'none';
            }, 500);
        }, 1000);
    });

    // Handle video error
    video.addEventListener('error', () => {
        console.log('Video failed to load, showing placeholder animation');
        placeholder.style.display = 'flex';
    });

    // Pause video when not in viewport (performance optimization)
    const videoObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                video.play().catch(err => console.log('Video play failed:', err));
            } else {
                video.pause();
            }
        });
    }, { threshold: 0.25 });

    videoObserver.observe(video);
}

// =============================================
// SMOOTH SCROLL
// =============================================
function initSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');

            // Skip if it's just #
            if (href === '#' || href === '#commencer' || href === '#connexion') {
                return;
            }

            const target = document.querySelector(href);

            if (target) {
                e.preventDefault();

                const offsetTop = target.offsetTop - 80; // Account for fixed navbar

                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// =============================================
// PERFORMANCE OPTIMIZATIONS
// =============================================

// Debounce function for scroll/resize events
function debounce(func, wait = 10) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Optimize scroll events
let ticking = false;
window.addEventListener('scroll', () => {
    if (!ticking) {
        window.requestAnimationFrame(() => {
            // Your scroll handlers here
            ticking = false;
        });
        ticking = true;
    }
});

// =============================================
// FLOATING CARDS PARALLAX EFFECT
// =============================================
window.addEventListener('mousemove', debounce((e) => {
    const cards = document.querySelectorAll('.floating-card');
    const { clientX, clientY } = e;
    const centerX = window.innerWidth / 2;
    const centerY = window.innerHeight / 2;

    cards.forEach((card, index) => {
        const speedFactor = (index + 1) * 0.02;
        const moveX = (clientX - centerX) * speedFactor;
        const moveY = (clientY - centerY) * speedFactor;

        card.style.transform = `translate(${moveX}px, ${moveY}px)`;
    });
}, 10));

// =============================================
// CONSOLE BRANDING
// =============================================
console.log('%cDoctHair', 'font-size: 48px; font-weight: bold; background: linear-gradient(135deg, #E87722 0%, #FF9447 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;');
console.log('%cAnalyse Capillaire Premium 2025', 'font-size: 14px; color: #667eea;');
console.log('Built with ❤️ for your hair health');

// =============================================
// PRELOAD CRITICAL ASSETS
// =============================================
window.addEventListener('load', () => {
    // Add loaded class to body for additional animations
    document.body.classList.add('loaded');

    // Preload video if available
    const video = document.querySelector('.background-video');
    if (video && video.readyState < 4) {
        video.load();
    }
});

// =============================================
// ANALYTICS & TRACKING (Placeholder)
// =============================================
function trackEvent(category, action, label) {
    console.log(`Event tracked: ${category} - ${action} - ${label}`);
    // Integrate with your analytics tool (GA4, Mixpanel, etc.)
    // if (window.gtag) {
    //     gtag('event', action, {
    //         'event_category': category,
    //         'event_label': label
    //     });
    // }
}

// Track CTA clicks
document.addEventListener('click', (e) => {
    if (e.target.closest('.btn-cta-primary')) {
        trackEvent('CTA', 'click', 'Start Diagnostic');
    }
    if (e.target.closest('.btn-cta-secondary')) {
        trackEvent('CTA', 'click', 'View Report Example');
    }
});

// =============================================
// RESIZE HANDLER
// =============================================
let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        // Reinit particles on resize
        const particlesContainer = document.getElementById('particles');
        if (particlesContainer) {
            particlesContainer.innerHTML = '';
            initParticles();
        }
    }, 250);
});
