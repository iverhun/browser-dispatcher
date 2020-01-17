import os
import runcmd


def read_profile_selector_dialog(applescript, args, background=False):
    if os.path.exists(applescript):
        path = applescript
    else:
        raise Exception("Apple script not found: {}".format(applescript))

    cmd = ["osascript", path]
    cmd.extend(args)

    r = runcmd.run(cmd, background=background)
    return r.code, r.out, r.err


if __name__ == "__main__":
    code, out, err = read_profile_selector_dialog('osascripts/choose.scpt', ['hello', 'hi', 'world'])
    print(code)
    print(out)
    print(err)
    print("---")
