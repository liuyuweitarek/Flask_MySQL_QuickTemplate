import os, sys, argparse

def run(args):
    if args.config == "dev":
        os.environ["EXAMPLE_MODE"] = "cfg.DevelopmentConfig"
    elif args.config == "prod":
        os.environ["EXAMPLE_MODE"] = "cfg.ProductionConfig"
    else:
        sys.exit("Please check out cfg.py and assign the valid params to --config. 'dev' or 'prod' Bye~")

    from app import app
    app.run(host=app.config['HOST'], port=app.config['PORT'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--config', type=str, default="dev", help="Please select your mode: 'dev' or 'prod' ")
    args = parser.parse_args()
    run(args)

    