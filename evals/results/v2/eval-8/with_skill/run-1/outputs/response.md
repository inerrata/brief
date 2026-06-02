*Assuming: goal = lift checkout-completion rate; the heavy drop is on the combined shipping+payment step. Adjust if wrong.*

The middle step asks for a lot at once (address + shipping + card), which is exactly where carts die. Five test hypotheses, each with a why and a metric:

1. **Split the mega-step into two screens (shipping, then payment).** Why: one big form feels heavier than two short ones; progress feels achievable. Metric: middle-step completion rate.
2. **Add a visible progress indicator (Step 2 of 3).** Why: uncertainty about how much is left increases abandonment. Metric: step-2 → confirm rate.
3. **Surface trust + total cost early (security badges, full price incl. shipping before payment).** Why: surprise costs and payment anxiety are top drop reasons. Metric: payment-field start rate.
4. **Offer express/wallet pay (Apple Pay / Google Pay / PayPal) at the top.** Why: skips manual card entry, the highest-friction field. Metric: checkout-completion rate, mobile especially.
5. **Enable guest checkout / autofill + inline validation.** Why: forced account creation and late error messages kill momentum. Metric: form-error rate and completion.

**Run them right:** change one variable at a time, pre-calculate the sample size you need, and let each test reach significance — don't call a winner off a few days of traffic. Judge on checkout-completion and revenue per session, not raw add-to-cart clicks (a vanity number).

Want these prioritized by likely impact vs. effort?
