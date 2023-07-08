test = {
  'name': 'Python Basics',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 10 + 2
          4d9a9f010a771e1434934b7e874ade0f
          # locked
          >>> 7 / 2
          c4a5533ecee83953f8fa3965bd6d64cc
          # locked
          >>> 7 // 2
          be9b9b860e53fef39d5863d61f03d3c4
          # locked
          >>> 7 % 2			# 7 modulo 2, equivalent to the remainder of 7 // 2
          6f717e91fe5a90641e44dc5a5368b663
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> x = 20
          >>> x + 2
          3d3ab69a0677d75a0ef4a99e0d2d1451
          # locked
          >>> x
          e1ac00f801290865dd772310ea7c60e4
          # locked
          >>> y = 5
          >>> y += 3			# Equivalent to y = y + 3
          >>> y * 2
          309984ef0dc06025a91b127042939a0e
          # locked
          >>> y //= 4			# Equivalent to y = y // 4
          >>> y + x
          3d3ab69a0677d75a0ef4a99e0d2d1451
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
