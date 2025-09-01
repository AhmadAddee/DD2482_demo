import argparse, sys
from typing import Iterable

import math_ops, str_ops, io_ops

def main(argv=None):
    parser = argparse.ArgumentParser(prog="sut", description="DevOps demo CLI")
    sub = parser.add_subparsers(dest="domain", required=True)

    # math
    p_math = sub.add_parser("math", help="math operations")
    sm = p_math.add_subparsers(dest="op", required=True)
    for op in ("add", "sub", "mul", "div"):
        sp = sm.add_parser(op)
        sp.add_argument("a", type=float)
        sp.add_argument("b", type=float)
    sm_mean = sm.add_parser("mean")
    sm_mean.add_argument("values", type=Iterable)
    sm_std = sm.add_parser("stddev")
    sm_std.add_argument("values", type=float, nargs="+")

    # string
    p_str = sub.add_parser("string", help="string utilities")
    ss = p_str.add_subparsers(dest="op", required=True)
    for op in ("sanitize", "slugify", "palindrome", "count"):
        sp = ss.add_parser(op)
        sp.add_argument("text", type=str)

    # io
    p_io = sub.add_parser("io", help="I/O utilities")
    si = p_io.add_subparsers(dest="op", required=True)
    for op in ("count-lines", "read-text", "read-json"):
        sp = si.add_parser(op)
        sp.add_argument("path", type=str)
    wr_txt = si.add_parser("write-text")
    wr_txt.add_argument("path", type=str)
    wr_txt.add_argument("data", type=str)
    wr_json = si.add_parser("write-json")
    wr_json.add_argument("path", type=str)
    wr_json.add_argument("data", type=str)

    args = parser.parse_args(argv)

    if args.domain == "math":
        if args.op == "add":
            print(math_ops.add(args.a, args.b))
        elif args.op == "sub":
            print(math_ops.sub(args.a, args.b))
        elif args.op == "mul":
            print(math_ops.mul(args.a, args.b))
        elif args.op == "div":
            print(math_ops.div(args.a, args.b))
        elif args.op == "mean":
            print(math_ops.mean(args.values))
        elif args.op == "stddev":
            print(math_ops.stddev(args.values))
    elif args.domain == "string":
        if args.op == "sanitize":
            print(str_ops.sanitize(args.text))
        elif args.op == "slugify":
            print(str_ops.slugify(args.text))
        elif args.op == "palindrome":
            print(str(str_ops.is_palindrome(args.text)).lower())
        elif args.op == "count":
            print(str_ops.word_count(args.text))
    elif args.domain == "io":
        if args.op == "count-lines":
            print(io_ops.count_lines(args.path))
        if args.op == "read-text":
            print(io_ops.read_text(args.path))
        if args.op == "read-json":
            print(io_ops.read_json(args.path))
        if args.op == "write-text":
            print(io_ops.write_text(args.path, args.data))
        if args.op == "write-json":
            print(io_ops.write_json(args.path, args.data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())