document.querySelectorAll('[data-keyring-calculator]').forEach((calculator) => {
  const { locale, units, perUnit, message, tiers: tierData } = calculator.dataset;
  const tiers = JSON.parse(tierData);
  const track = calculator.querySelector('#landing-slider-track');
  const progress = calculator.querySelector('#landing-slider-prog');
  const thumb = calculator.querySelector('#landing-slider-thumb');
  const quantity = calculator.querySelector('#landing-calc-qty');
  const price = calculator.querySelector('#landing-calc-price');
  const unit = calculator.querySelector('#landing-calc-unit');
  const quote = calculator.querySelector('#landing-calc-quote');
  const formatQuantity = new Intl.NumberFormat(locale);
  const formatTotal = new Intl.NumberFormat(locale, { style: 'currency', currency: 'EUR', maximumFractionDigits: 0 });
  const formatUnit = new Intl.NumberFormat(locale, { style: 'currency', currency: 'EUR' });
  let selected = 0;

  function selectTier(index) {
    selected = Math.max(0, Math.min(index, tiers.length - 1));
    const [count, unitPrice] = tiers[selected];
    const position = (selected / (tiers.length - 1)) * 100 + '%';
    const quantityLabel = formatQuantity.format(count) + ' ' + units;
    quantity.textContent = quantityLabel;
    price.textContent = formatTotal.format(count * unitPrice);
    unit.textContent = '(' + formatUnit.format(unitPrice) + '/' + perUnit + ')';
    progress.style.width = position;
    thumb.style.left = position;
    track.setAttribute('aria-valuenow', selected);
    track.setAttribute('aria-valuetext', quantityLabel);
    quote.href = 'https://wa.me/34680317486?text=' + encodeURIComponent(message.replace('{qty}', count));
  }

  function selectFromPointer(event) {
    const { left, width } = track.getBoundingClientRect();
    if (width > 0) selectTier(Math.round((event.clientX - left) / width * (tiers.length - 1)));
  }

  track.style.touchAction = 'pan-y';
  track.addEventListener('pointerdown', (event) => {
    track.setPointerCapture(event.pointerId);
    selectFromPointer(event);
  });
  track.addEventListener('pointermove', (event) => {
    if (track.hasPointerCapture(event.pointerId)) selectFromPointer(event);
  });
  track.addEventListener('keydown', (event) => {
    const steps = { ArrowLeft: selected - 1, ArrowDown: selected - 1, ArrowRight: selected + 1, ArrowUp: selected + 1, Home: 0, End: tiers.length - 1 };
    if (!Object.hasOwn(steps, event.key)) return;
    event.preventDefault();
    selectTier(steps[event.key]);
  });
  calculator.querySelectorAll('[data-keyring-tier]').forEach((button) => {
    button.addEventListener('click', () => selectTier(Number(button.dataset.keyringTier)));
  });
  selectTier(0);
});
