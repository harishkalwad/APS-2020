def findPages(N, K, P):
    cnt = 0
    offset = 1
    for chapter in P:
        pages = (chapter + K -1)/K
        for idx in xrange(pages):
            if offset >= (idx * K)+1 and offset <= min((idx+1)*K, chapter):
                cnt += 1
            offset += 1
 
    return cnt
 
if __name__ == '__main__':
    N, K = map(int, raw_input().split())
    P = map(int, raw_input().split())
    print findPages(N, K, P)
