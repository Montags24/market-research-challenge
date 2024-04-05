import giftCard from '../assets/svg/gift-card.svg'
import lottery from '../assets/svg/lottery.svg'
import subscription from '../assets/svg/subscription.svg'
import comingSoon from '../assets/svg/coming-soon.svg'

const prizes = [
  {
    name: '£10 Gift Card',
    cost: '100',
    image: giftCard
  },
  {
    name: 'Monthly Subscription',
    cost: '200',
    image: subscription
  },
  {
    name: '£100 prize draw',
    cost: '500',
    image: lottery
  },
  {
    name: 'More prizes coming soon...',
    cost: '?',
    image: comingSoon
  }
]

export default prizes
