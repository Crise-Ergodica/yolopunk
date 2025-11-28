// YoloPunk Custom JavaScript
// Ergodic interactions and animations

(function () {
  "use strict";

  // Initialize when DOM is ready
  document.addEventListener("DOMContentLoaded", function () {
    initErgodicEffects();
    initChaosLevel();
    initBloodTrail();
  });

  /**
   * Initialize ergodic visual effects
   */
  function initErgodicEffects() {
    // Add chaos particle effect to headers
    const headers = document.querySelectorAll(".grimorio-header");
    headers.forEach((header) => {
      createChaosParticles(header);
    });
  }

  /**
   * Create chaos particles effect
   */
  function createChaosParticles(element) {
    const particleCount = 20;
    const container = document.createElement("div");
    container.className = "chaos-particles";
    container.style.cssText = `
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      overflow: hidden;
    `;

    for (let i = 0; i < particleCount; i++) {
      const particle = document.createElement("div");
      particle.style.cssText = `
        position: absolute;
        width: 2px;
        height: 2px;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        top: ${Math.random() * 100}%;
        left: ${Math.random() * 100}%;
        animation: float ${3 + Math.random() * 4}s ease-in-out infinite;
        animation-delay: ${Math.random() * 2}s;
      `;
      container.appendChild(particle);
    }

    element.appendChild(container);
  }

  /**
   * Initialize chaos level indicator
   */
  function initChaosLevel() {
    const indicator = document.querySelector(".chaos-level");
    if (!indicator) return;

    const level = indicator.dataset.level || "medium";
    const colors = {
      low: "#6a0dad",
      medium: "#c41e3a",
      high: "#8b0000",
    };

    indicator.style.background = `radial-gradient(circle, ${colors[level]}, transparent)`;

    // Add tooltip
    indicator.title = `Chaos Level: ${level.toUpperCase()}`;
  }

  /**
   * Initialize blood trail effect on scroll
   */
  function initBloodTrail() {
    let lastScrollTop = 0;
    const bloodDrip = document.querySelector(".blood-drip");

    if (!bloodDrip) return;

    window.addEventListener(
      "scroll",
      function () {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const scrollPercent = (scrollTop / (document.documentElement.scrollHeight - window.innerHeight)) * 100;

        bloodDrip.style.width = scrollPercent + "%";
        bloodDrip.style.boxShadow = `0 0 ${10 + scrollPercent / 10}px rgba(196, 30, 58, 0.6)`;

        lastScrollTop = scrollTop;
      },
      false,
    );
  }

  /**
   * Add convergence animation to code blocks
   */
  function initCodeBlockEffects() {
    const codeBlocks = document.querySelectorAll("pre code");

    codeBlocks.forEach((block) => {
      block.addEventListener("mouseenter", function () {
        this.style.boxShadow = "0 0 20px rgba(0, 255, 255, 0.3)";
      });

      block.addEventListener("mouseleave", function () {
        this.style.boxShadow = "none";
      });
    });
  }

  // Add CSS animations
  const style = document.createElement("style");
  style.textContent = `
    @keyframes float {
      0%, 100% {
        transform: translateY(0) translateX(0);
        opacity: 0;
      }
      10% {
        opacity: 0.3;
      }
      90% {
        opacity: 0.3;
      }
      50% {
        transform: translateY(-20px) translateX(10px);
        opacity: 0.6;
      }
    }
  `;
  document.head.appendChild(style);
})();
