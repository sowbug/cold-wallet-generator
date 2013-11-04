import format_key

kf = format_key.KeyFormatter()

tests = [
# BIP 0038 Example #1
("TestingOneTwoThree",
"6PRVWUbkzzsbcVac2qwfssoUJAN1Xhrg6bNk8J7Nzm5H7kxEbn2Nh2ZoGg",
"5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR",
"CBF4B9F70470856BB4F40F80B87EDB90865997FFEE6DF315AB166D713AF433A5",
"1Jq6MksXQVWzrznvZzxkV6oY57oWXD9TXB",
"04D2CE831DD06E5C1F5B1121EF34C2AF4BCB01B126E309234ADBC3561B60C9360EA7F23327B49BA7F10D17FAD15F068B8807DBBC9E4ACE5D4A0B40264EEFAF31A4"),

# BIP 0038 Example #2
("Satoshi",
"6PRNFFkZc2NZ6dJqFfhRoFNMR9Lnyj7dYGrzdgXXVMXcxoKTePPX1dWByq",
"5HtasZ6ofTHP6HCwTqTkLDuLQisYPah7aUnSKfC7h4hMUVw2gi5",
"09C2686880095B1A4C249EE3AC4EEA8A014F11E6F986D0B5025AC1F39AFBD9AE",
"1AvKt49sui9zfzGeo8EyL8ypvAhtR2KwbL",
"0463B600A0BB6A2F2BEF7BB9648222C3593A6EF5F7C2D81433C5193BF84B9F862B940E55DA162AECA6293CDE138BCC18BA978FAE399F14F258AFA4F799EE61ADCB"),

# bitaddress.org test vector #1
(None,
 None,
 "5J8QhiQtAiozKwyk3GCycAscg1tNaYhNdiiLey8vaDK8Bzm4znb",
 "292665C3872418ADF1DA7FFA3A646F2F0602246DA6098A91D229C32150F2718B",
 "1Cnz9ULjzBPYhDw1J8bpczDWCEXnC9HuU1",
 "0478982F40FA0C0B7A55717583AFC99A4EDFD301A2729DC59B0B8EB9E18692BCB521F054FAD982AF4CC1933AFD1F1B563EA779A6AA6CCE36A30B947DD653E63E44"),

# bitaddress.org leading zero in public key bug
(None,
 None,
 "5Je7CkWTzgdo1RpwjYhwnVKxQXt8EPRq17WZFtWcq5umQdsDtTP",
 "6C9565B3EEF4EF9E01C216E1910763A5F94CF3654C059E8C67A348D10AE39C28",
 "1M6dsMZUjFxjdwsyVk8nJytWcfr9tfUa9E",
 "040076D4852E6E0311E080036EFEC96A339540176CF53EB7182580BC81326EC9B16D78DF5918E18EF1F57AE0591541D268DEE528BF5C29E963899946D300F90358"),

# bitaddress.org leading zero in private key bug
(None,
 None,
 "5HpJ4bpHFEMWYwCidjtZHwM2rsMh4PRfmZKV8Y21i7msiUkQKUW",
 "0004D30DA67214FA65A41A6493576944C7EA86713B14DB437446C7A8DF8E13DA",
 "1NAjZjF81YGfiJ3rTKc7jf1nmZ26KN7Gkn",
 "049848B6EAE15C2E078FE12EF779F4E322DEF5241C0B213D36D327A78B4EB744D379FD3C3C0D44FC99FDAE161C45BBC458CF84BA5F437229FD6D1DE9CE483C2F0B")
 ]

for test in tests:
    # Unencrypted, hex
    lines = [test[3]]
    out = kf.format(["%a:%h:%p:%w"], lines, None)
    expected = "%s:%s:%s:%s" % (test[4], test[3], test[5], test[2])
    assert expected == out, "Unencrypted/hex: expected %s but got %s" % (
        expected, out) 

    # Unencrypted, WIF
    lines = [test[2]]
    out = kf.format(["%a:%h:%p:%w"], lines, None)
    expected = "%s:%s:%s:%s" % (test[4], test[3], test[5], test[2])
    assert expected == out, "Unencrypted/WIF: expected %s but got %s" % (
        expected, out) 

    if test[0]:
        # Encrypted, hex
        lines = [test[3]]
        out = kf.format(["%a:%h:%p:%w"], lines, test[0])
        expected = "%s:%s:%s:%s" % (test[4], test[3], test[5], test[1])
        assert expected == out, "Encrypted/hex: expected %s but got %s" % (
            expected, out) 

        # Encrypted, WIF
        lines = [test[2]]
        out = kf.format(["%a:%h:%p:%w"], lines, test[0])
        expected = "%s:%s:%s:%s" % (test[4], test[3], test[5], test[1])
        assert expected == out, "Encrypted/hex: expected %s but got %s" % (
            expected, out) 
        
