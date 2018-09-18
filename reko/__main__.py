import sys
import traceback
from .cli import parser
from .core import program

def main(argv=sys.argv):

    if len(argv) == 1:
        # 2017.04.29訂正
        # len(argv) == 0ではなく1でした。失礼しました

        parser.parse_args(["-h"]) # コマンドライン引数が無かった場合はヘルプメッセージを出力
        sys.exit(0)

    args = parser.parse_args(argv)

    try:
        exit_code = program(args)
        sys.exit(exit_code)

    except Exception as e:
        error_type = type(e).__name__ # 29.6.2追記：これでエラー名を取得できる
        stack_trace = traceback.format_exc()

        if args.stacktrace:
            print("{:=^30}".format(" STACK TRACE "))
            print(stack_trace)
        else:
            sys.stderr.write(
                "{0}: {1}\n".format(e.type, e.message))
            sys.exit(1)


if __name__ == '__main__': main()