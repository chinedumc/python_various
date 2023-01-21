import os
bidders_n_bid = {}

def all_bids():
  ask_name = input("Enter name of bidder: ")
  ask_bid_price = int(input("Enter bid price: $"))

  bidders_n_bid[ask_name] = ask_bid_price

all_bids()

no_more_bids = False

while not no_more_bids:
  if_more_bidders = input('Any more bids? Type "yes" or "no": ').lower()

  if(if_more_bidders == 'yes'):
    os.system('cls')
    all_bids()

  elif(if_more_bidders == 'no'):
    #FIND THE HIGHEST BIDDER
    # max_key = next(iter(bidders_n_bid))
    # for key in bidders_n_bid:
    #   if bidders_n_bid[key] > bidders_n_bid[max_key]:
    #     max_key = key

    ## OR:
    for key in bidders_n_bid:
      highest_bid = 0
      # bid = bidders_n_bid[key]
      if bidders_n_bid[key] > highest_bid:
        highest_bid = bidders_n_bid[key]

    no_more_bids = True
    # print(f'The bid winner is: {max_key}')
    print(f'The bid winner is: {key} with a bid of ${highest_bid}')
  else:
    print('Enter a "yes" or "no".')

# print(bidders_n_bid)