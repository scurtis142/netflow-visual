import csv
import operator


class Netflow:
   def __init__(self, src_ip, dst_ip, src_port, dst_port, proto, octs, pkts):
      self.src_ip = src_ip
      self.dst_ip = dst_ip
      self.src_port = src_port
      self.dst_port = dst_port
      if proto == "6":
         self.proto = "tcp"
      elif proto == "17":
         self.proto = "udp"
      elif proto == "1":
         self.proto = "icmp"
      else :      
         self.proto = proto
      self.pkts = pkts
      self.octs = octs

   def toString(self):
      return self.src_ip.ljust(18)\
         +self.dst_ip.ljust(18)\
         +self.src_port.ljust(14)\
         +self.dst_port.ljust(19)\
         +self.proto.ljust(11)\
         +self.pkts.ljust(12)\
         +self.octs


entries = []

def main ():
   with open ("/tmp/netflow.csv", "r") as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      sorted_csv = sorted(csv_reader, key=lambda row: int(row[6]), reverse=True)
      counter = 0
      for row in sorted_csv:
         if counter == 10:
            break
         entry = Netflow(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
         entries.append(entry)
         counter += 1

   header_string = "Source IP".ljust(18)\
                  +"Destination IP".ljust(18)\
                  +"Source Port".ljust(14)\
                  +"Destination Port".ljust(19)\
                  +"Protocol".ljust(11)\
                  +"Packets".ljust(12)\
                  +"Bytes\n"

   print(header_string)
   for entry in entries:
      print(entry.toString());



if __name__ == "__main__":
   main()
