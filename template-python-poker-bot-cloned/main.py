#!/usr/bin/env python3
import asyncio
import argparse

from tg.bot import Bot
import time

parser = argparse.ArgumentParser(
    prog='Template bot',
    description='A Turing Games poker bot that always checks or calls, no matter what the target bet is (it never folds and it never raises)')

parser.add_argument('--port', type=int,
                    help='The port to connect to the server on')
parser.add_argument('--host', type=str, default='localhost',
                    help='The host to connect to the server on')
parser.add_argument('--room', type=str, default='my-new-room',
                    help='The room to connect to')
parser.add_argument('--party', type=str, default='poker',
                    help='The party to connect to')
parser.add_argument('--key', type=str, default='',
                    help='The key for authentication')

args = parser.parse_args()

# Always call
class TemplateBot(Bot):
    def act(self, state, hand):
        print('asked to act')
        print('acting', state, hand, self.my_id)
        return {'type': 'call'}

    def opponent_action(self, action, player):
        print('opponent action?', action, player)

    def game_over(self, payouts):
        print('game over', payouts)

    def start_game(self, my_id):
        self.my_id = my_id
        print('start game', my_id)

if __name__ == "__main__":
    bot = TemplateBot(args.host, args.port, args.room, args.party, args.key)
    asyncio.run(bot.start())
